# -*- coding: utf-8 -*-
"""Лабораторная-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gAoq3nGUKJXD8Jmepg0UMG3UwxSbc7t0

Лабораторная посвящена базе данных, связанной с футбольным командами. Схема расположена на картинке ниже.

## Описание таблиц

**Coaches - Таблица тренеров**

*id* - уникальный идентификатор тренера

*Name* - имя тренера

**Teams - Таблица команд**

*id* - уникальный идентификатор  команды

*Name* - имя команды

*Location* - расположение команды

*Coach_id* - идентификатор тренера

**Players - Таблица игроков**

*Id* - уникальный идентификатор игрока

*Name* - имя игрока

*Position_id* - идентификатор позиции

*Age* - возраст игрока

*Team_id* - идентификатор команды

*Start_date* - дата начала игры в команде

## Схема
![hw_diagram.jpg](data:image/jpeg;base64,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)

# Задание 1
Реализовать таблицы со связями по схеме выше.
"""

# Commented out IPython magic to ensure Python compatibility.
# %load_ext sql
# %sql sqlite:///base.db

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# Pragma foreign_keys=on;
# 
# CREATE TABLE IF NOT EXISTS Players (
#   player_id integer NOT NULL Primary Key,
#   name varchar(128),
#   position_id integer,
#   age integer,
#   team_id integer NOT NULL,
#   start_date integer
# );
# 
# CREATE TABLE IF NOT EXISTS Teams (
#   team_id integer NOT NULL Primary Key,
#   name varchar(128),
#   location varchar(256),
#   coach_id integer NOT NULL,
#   FOREIGN KEY (team_id) REFERENCES Players(team_id)
#   FOREIGN KEY (coach_id) REFERENCES Players(coach_id)
# );
# 
# CREATE TABLE IF NOT EXISTS Coaches (
#   coach_id integer NOT NULL Primary Key,
#   name varchar(128) NOT NULL UNIQUE
# );

"""# Задание 2
Написать функцию, осуществляющую добавление тренера. На вход функции подается имя тренера. При невозможности вставки функция должна обработать данное исключение и вывести пользователю информацию о проблеме

После написания функции необходимо добавить несколько тренеров для таблицы.
"""

import sqlite3
db = sqlite3.connect('base.db')

def insertCoach(name):
  try:
      if not isinstance(name, str) or not name.isalpha():
        raise ValueError
      cur = db.cursor()
      cur.execute('''
      SELECT COALESCE(MAX(coach_id) + 1, 1) from Coaches''')
      ID = cur.fetchone()[0]
      cur.execute('''
        INSERT INTO Coaches(coach_id, name)
        VALUES(?,?)''', (ID, name))
      db.commit()
  except ValueError:
    print("Введено недопустимое имя")
  except Exception:
    print('Что-то пошло не так.')

insertCoach('Barbossa')
insertCoach('Amygdala')
insertCoach('Light')

insertCoach('B3br@')

insertCoach(1235)

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# SELECT * FROM Coaches;

"""# Задание 3

Написать функцию, осуществляющую добавление команды. На вход функция принимает (имя команды, местоположение, имя тренера).
На выходе должна быть добавлена команда.

После написания функции необходимо добавить несколько команд (хотя бы по 1 на каждого тренера).
"""

def insertTeam(team_name, location, coach_name):
  try:
    if not isinstance(team_name, str) or not isinstance(location, str) or \
        not isinstance(coach_name, str) or not coach_name.isalpha():
      raise ValueError
    cur = db.cursor()
    cur.execute('''
    SELECT COALESCE(MAX(team_id) + 1, 1) from Teams''')
    ID = cur.fetchone()[0]
    coach_id = getCoachId(coach_name)
    if coach_id is not None:
      cur.execute('''
        INSERT INTO Teams(team_id, name, location, coach_id)
        VALUES(?,?, ?, ?)''', (ID, team_name, location, coach_id))
      db.commit()
    else:
      raise ValueError
  except ValueError:
    print("Введено недопустимое значение")
  except Exception:
    print('Что-то пошло не так.')

def getCoachId(name):
  cur = db.cursor()
  try:
    print(name)
    cur.execute('''
    SELECT coach_id FROM Coaches WHERE name = ? ''', (name,))
    return int(cur.fetchone()[0])
  except Exception:
    print('Тренера с таким именем не существует')

insertTeam('Pirates', 'Carabbian Sea', 'Barbossa')
insertTeam('Nightmares', 'Yharnam', 'Amygdala')
insertTeam('L team', 'Jp, Tokyo', 'Light')

insertTeam('Leroro', 'America, Texas', 'Light')

insertTeam('GG', 'Moscow', 'Brom')

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# SELECT * FROM Teams;

"""# Задание 4

Написать функцию, осуществляющую обновление информации о команде. У функции на входе должен быть один обязательный параметр - название команды и два необязательных параметра - имя тренера и местоположение. При этом хотя бы один из необязательных параметров должен быть заполнен. Функция должна обновлять значение переданных необязательных параметров.

После написания функции вызовите данную функцию несколько раз.
"""

def updateTeam(team_name, coach_name = None, location = None):
  try:
    if coach_name is None and location is None:
      raise ValueError('Оба параметра не введены')
    coach_id = getCoachId(coach_name)

    team_id = check_team(team_name)
    if team_id == 0:
      raise ValueError('Такой команды не существует')
    cur = db.cursor()

    if location is None:
      cur.execute('''
      UPDATE Teams SET coach_id = ? WHERE team_id = ?''', (coach_id, team_id))
    elif coach_id is None:
      cur.execute('''
      UPDATE Teams SET location = ? WHERE team_id = ?''', (location, team_id))
    else:
      cur.execute('''
      UPDATE Teams SET location = ? WHERE team_id = ?''', (location, team_id))
      cur.execute('''
      UPDATE Teams SET coach_id = ? WHERE team_id = ?''', (coach_id, team_id))

    db.commit()
  except ValueError as e:
    print(e)

def check_team(name):
  cur = db.cursor()
  cur.execute('''
  SELECT team_id FROM Teams WHERE name = ?''', (name,))
  try:
    id = cur.fetchone()[0]
    return id
  except TypeError:
    print('Возможно опечатка')
    return 0
  except:
    print('Такой команды не существует')
    return 0
  return cur

updateTeam('Leroro')

insertCoach('Bogdan')

updateTeam('L team', coach_name='Bogdan')

updateTeam('L team', location='Magadan')

insertCoach('Jotaro')
updateTeam('Leroro', coach_name='Jotaro', location='Egypt, pyramids')

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# SELECT * FROM Teams;

"""# Задание 5

Написать функцию, осуществляющую добавление нового футболиста в таблицу игроков. На входе (имя, возраст, позиция, название команды, дата перехода в команду(необязательный параметр)). Если дата перехода не указана, то нужно использовать текущую дату. Предусмотреть различные ошибки (такие как неверное имя позиции, неверное название команды (игрока нельзя добавить, если его команды нет в таблице команд), возраст < 0 и т.п.)

После написания функции необходимо добавить несколько игроков (хотя бы по 1 на команду).
"""

import datetime

str(datetime.date.today()) # сегодня

def insertPlayer(name, age, position, team_name, date=datetime.date.today()):
  try:
    if not isinstance(age, int) or age <= 0:
      raise ValueError('Некорректный возраст')
    if not isinstance(position, int) or position < 0 or position >= 9:
      raise ValueError('Некорректная позиция')
    if not isinstance(name, str) and \
    ''.join([i for i in name if i != ' ']).isalpha():
      raise ValueError('Некорректное имя')
    if date > datetime.date.today():
      raise ValueError('Некорректная дата')

    cur = db.cursor()
    cur.execute('SELECT COALESCE(MAX(player_id) + 1, 1) from Players')
    id = cur.fetchone()[0]
    team_id = check_team(team_name)
    cur.execute('''
      INSERT INTO
      Players(player_id, name, position_id, age, team_id, start_date)
      VALUES(?,?,?,?,?,?)''', (id, name, position, age, team_id, date))
    db.commit()
  except ValueError as e:
    print(e)
  except Exception as e:
    print(e)

insertPlayer('Doll', 50, 4, 'Nightmares', datetime.date(2021, 3, 29))

insertPlayer('Jack Sparrow', 40, 20, 'Pirates', datetime.date(1990, 12, 12))

insertPlayer('Jack Sparrow2', 40, -4, 'Pirates', datetime.date(1990, 12, 12))

insertPlayer('Captain Jack Sparrow', 41, 4, 'Pirates', datetime.date(1990, 12, 12))

insertPlayer('N', 14, 2, 'L team')

insertPlayer('Scorpion', 38, 7, 'Leroro', datetime.date(2000, 10, 30))

# Commented out IPython magic to ensure Python compatibility.
# %%sql
# SELECT * FROM Players;

"""# Задание 6*

Написать небезопасную функцию, осуществляющую просмотр информации о футболистах по имени команды (только из этой команды).

Написать 2 запроса - один "корректный", другой с инъекцией, приводящей к выводу информации по всем игрокам.
"""

