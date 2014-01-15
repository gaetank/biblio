from django.core.management import os
#from tutoriel import settings
#setup_environ(settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutoriel.settings")

from biblio.models import Author, Book, Subject
import json

authors = json.load(open("authors.json", encoding="utf-8"))
author_table = {}

for a in authors:
	author = Author(lastname=a["lastname"], firstname=a["firstname"])
	author.save()
	author_table[str(author)] = author

books = json.load(open("books.json", encoding="utf-8"))

subject_table={}
for b in books:
	s = b["subject"]
	if s not in subject_table:
		subject = Subject(label=s)
		subject.save()
		subject_table[s] = subject

for b in books:
	book = Book(title=b["title"], subject=subject_table[b["subject"]])
	book.save()
	for name in b["authors"]:
		author = author_table[name]
		book.authors.add(author)
	book.save()

#chargement des permissions

from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType

author_content_type = ContentType.objects.get_for_model(Author)

perms = json.load(open("perms.json", encoding="utf-8"))
PERMS = {}
for p in perms:
	perm = Permission.objects.create(codename=p["codename"], name=p["name"], content_type=author_content_type)
	perm.save()
	PERMS[p["codename"]] = perm

# charger des groupes

groups = json.load(open("groups.json", encoding="utf-8"))
GROUPS={}
for g in groups:
	group = Group.objects.create(name=g["name"])
	group.save()
	for p in g["permissions"]:
		group.permissions.add(PERMS[p])
	group.save()
	GROUPS[g["name"]] = group

# charger des utilisateurs

users = json.load(open("users.json", encoding="utf-8"))
USERS={}
for u in users:
	user = User.objects.create_user(username=u["username"], password=u["password"])
	user.save()
	for g in u["groups"]:
		user.groups.add(GROUPS[g])
	user.save()
	USERS[u["username"]] = user
	
