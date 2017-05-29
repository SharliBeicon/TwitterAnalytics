import tasks

hashtag = input("Introduce un hashtag: ")
result = tasks.hashtag.delay(hashtag)
holi = result.get()
result2 = tasks.procesar.delay(hashtag)
tuits = result2.get()

if result2.successful():
    print ("[*] Subida correcta. Nº de tweets captados: %s" % tuits)
else:
    print ("[*] La shet")
