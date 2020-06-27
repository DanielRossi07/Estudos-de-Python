from playsound import playsound
resp = str(input("Saúdade do bailão né meu filho? "))
if resp == ("sim"):
    playsound(r"C:\Users\Daniel\PycharmProjects\PythonExercises\venv\Lib\site-packages\pygame\examples\data\teste.mp3")
else: quit()
parar = print(input("deseja parar a música? "))
if parar == ("sim"):
    quit()
else: ()
