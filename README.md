# Использование Docker в приложении Flask с БД

## Порядок действий
1. Зугрузить файлы задания в репозиторий
2. Выбрать базу данных - была выбрана mongo из-за удобства работы с ней
3. Дописать в файлах код под базу данных:
   - в requirments.txt добавить строчку </br>
     ```pymongo```
   - в docker-compose.yml </br>
     ```
     mongohost:
       image: "mongo:latest"
       ports:
         - "27017:27017"
     ```
   - в app.py подключение к бд и запись данных в нее (файл src/app.py)
4. В Docker desktop запустить бд </br>
  ![image](https://github.com/user-attachments/assets/5171f9f7-dac5-4dd7-9c0a-6a6de8c8e748)
5.  Запустить сборку командой </br>
  ```docker-compose up --build```
6. Проверить, что в Docker desktop все запущено </br>
   ![image](https://github.com/user-attachments/assets/cad7e80c-384b-4595-8e4a-9d7fa2dcb26d)


Для проверки работы системы перейти в браузер на http://localhost:5000, где будет отображаться счетчик </br>
![image](https://github.com/user-attachments/assets/1b5293ba-d48f-4d89-935f-bc6d20e2bc1b)

Для просмотра записей в бд, необходимо перейти в браузер на http://localhost:5000/database </br>
![image](https://github.com/user-attachments/assets/3d8ba297-77a0-4a0a-996d-e976e49c09ee)


