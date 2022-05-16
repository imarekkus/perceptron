
# Tworzymy sieć i trenujemy ją:

Do tego służy plik `python model.py` który tworzy plik `model.pkl`.

# Tworzymy obraz dockerowy:

Na podstawie pliku `Dockerfile`. tworzymy obraz wpisując: `docker build --tag zadrta .` 

# Tworzymy kontener dockerowy:

Wpisując polecenie: `docker run -p 3000:3333 -d --name perceptron zadrta:latest`

# Sprawdzamy czy działa:

Wpisując `docker ps`
![image](https://user-images.githubusercontent.com/49692939/168680654-73dc885b-348c-4a10-9c19-044c5157f58e.png)


# Wchodzenie na stronę:

Można wejść na stronę wchodząc przez dockera, ale wtedy wyświetla nam się tylko tekst, a nie predykcje
![image](https://user-images.githubusercontent.com/49692939/168680505-c2965fc2-33ad-4abe-bb9a-b73efe10cc0c.png)
Żeby wyświetliły się predykcję przechodzimy do kolejnego kroku

# Wklejamy url z danymi do przeglądarki:

http://localhost:3000/predict?sepal_length=0.3&sepal_width=3.2&petal_length=5.7&petal_width=0.8

# W przeglądarce powinna wyskoczyć predykcja:
![image](https://user-images.githubusercontent.com/49692939/168679151-1a91c760-1fe8-4927-975e-af0599bfa528.png)

