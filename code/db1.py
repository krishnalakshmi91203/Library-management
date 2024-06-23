import sqlite3

MERGE=sqlite3.connect('merge.db')
merge= MERGE.cursor()
merge.execute("DROP TABLE IF EXISTS section")
merge.execute("DROP TABLE IF EXISTS book")
merge.execute("DROP TABLE IF EXISTS user")
merge.execute("DROP TABLE IF EXISTS main")

table = """ CREATE TABLE section(
			ID int(5) NOT NULL PRIMARY KEY,
			Name CHAR(25) NOT NULL,
			Date DATE ,
			Description CHAR(100)); """
table1 = """ CREATE TABLE book(ID INT(5) NOT NULL PRIMARY KEY,
			Name CHAR(100) NOT NULL,
			Content CHAR(100) ,
			Author CHAR(25),
                        SectionID INT,price INT(3),
                        rating INT(1),
                        FOREIGN KEY (SectionID) REFERENCES section(ID));"""
table2= """ CREATE TABLE user(
			Name CHAR(25) NOT NULL,
			Role char(25),
			uname char(25) NOT NULL PRIMARY KEY,
			Pwd CHAR(100)NOT NULL UNIQUE,
			number int(10),
			email char(50)); """
table3= """ CREATE TABLE main(sectionid int(5),
                    bookid int(5),username char(25),Date_issued DATE,
                    Return_date DATE,status char(10),PRIMARY KEY (bookid, username),
                    FOREIGN KEY (sectionid) REFERENCES book(SectionID),
                    FOREIGN KEY (bookid) REFERENCES book(ID),
                    FOREIGN KEY (username) REFERENCES user(uname)); """

merge.execute(table)
merge.execute(table1)
merge.execute(table2)
merge.execute(table3)

merge.execute('''INSERT INTO section VALUES (101, 'Fiction', '2022-05-15', 'explore the human experience ')''')
merge.execute('''INSERT INTO book VALUES (10100, 'The Catcher in the Rye', 'Catcher in the Rye Text.pdf', 'J.D. Salinger', 101,56, 3)''')
merge.execute('''INSERT INTO book VALUES (10101, 'To Kill a Mockingbird','TKMFullText.pdf', 'Harper Lee',101,73, 2)''')

merge.execute('''INSERT INTO section VALUES (102, 'Science', '2022-06-10', 'unravel the mysteries of physics, biology, chemistry')''')
merge.execute('''INSERT INTO book VALUES (10200, 'A Brief History of Time','stephen_hawking_a_brief_history_of_time.pdf', 'Stephen Hawking',102,67, 1)''')
merge.execute('''INSERT INTO book VALUES (10201, 'The Selfish Gene','The-Selfish-Gene-R.-Dawkins-1976-WW-.pdf', 'Richard Dawkins',102,90, 3)''')

merge.execute('''INSERT INTO section VALUES (103, 'History', '2022-07-05', 'comprehensive narrative of past events')''')
merge.execute('''INSERT INTO book VALUES (10300, 'The Guns of August', '20131016_TheGunsofAugust.pdf', 'Barbara W. Tuchman',103,78, 2)''')
merge.execute('''INSERT INTO book VALUES (10301, 'A People''s History of the United States', 'history_outline.pdf', 'Howard Zinn', 103,89, 1)''')

merge.execute('''INSERT INTO user VALUES ('Krishna lakshmi', 'Student', 'krishna', 'kl@123',9567204245,'kl@gmail.com')''')
merge.execute('''INSERT INTO user VALUES ('Rohit kumar', 'manager', 'rohit', 'roh@123', 9086878869, 'rohit@gmail.com')''')
MERGE.commit()
MERGE.close()
