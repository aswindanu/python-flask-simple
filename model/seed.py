import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    os.getenv("DATABASE_USERNAME") or os.getenv("POSTGRES_USERNAME"),
    os.getenv("DATABASE_PASSWORD") or os.getenv("POSTGRES_PASSWORD"),
    os.getenv("DATABASE_HOST") or os.getenv("POSTGRES_HOST"),
    os.getenv("DATABASE_PORT") or os.getenv("POSTGRES_PORT"),
    os.getenv("DATABASE_DATABASE") or os.getenv("POSTGRES_DATABASE"),
)
engine = create_engine(
    DATABASE_URL,
    echo=True
)

Session = scoped_session(sessionmaker(bind=engine))

s = Session()
s.execute(
"""
INSERT INTO "public"."berat_badan" ("id", "max", "min", "perbedaan", "tanggal") VALUES
(1, 50, 48, 2, '2018-08-18'),
(2, 51, 50, 1, '2018-08-19'),
(3, 52, 50, 2, '2018-08-20'),
(4, 49, 49, 0, '2018-08-21'),
(5, 50, 49, 1, '2018-08-22');

SELECT setval('berat_badan_id_seq', 6, true);

INSERT INTO "public"."user" ("id", "email", "username", "password", "fullname", "phone", "gender", "active", "ip_address", "created_at", "updated_at") VALUES
(1, 'testone@gmail.com', 'testone', 'testone', 'Test One', '08123456781', 'M', TRUE, '127.0.0.1', '2018-08-19', '2018-08-19'),
(2, 'testtwo@gmail.com', 'testtwo', 'testtwo', 'Test Two', '08123456782', 'F', TRUE, '127.0.0.1', '2018-08-19', '2018-08-19'),
(3, 'testthree@gmail.com', 'testthree', 'testthree', 'Test Three', '08123456783', 'M', TRUE, '127.0.0.1', '2018-08-19', '2018-08-19'),
(4, 'testfour@gmail.com', 'testfour', 'testfour', 'Test Four', '08123456784', 'F', TRUE, '127.0.0.1', '2018-08-19', '2018-08-19'),
(5, 'testfive@gmail.com', 'testfive', 'testfive', 'Test Five', '08123456785', 'M', TRUE, '127.0.0.1', '2018-08-19', '2018-08-19');

SELECT setval('user_id_seq', 6, true);
"""
)
s.commit()
