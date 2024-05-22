-- creates the mysql server user_0d_1
-- the user should have all privileges and password set to user_0d_pwd

CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
