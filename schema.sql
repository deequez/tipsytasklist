CREATE TABLE users (id INTEGER PRIMARY KEY, 
                    email VARCHAR(64), 
                    password VARCHAR(255), 
                    name VARCHAR(64)
                    );

CREATE TABLE tasks (id INTEGER PRIMARY KEY, 
					title VARCHAR(255),
					created_at DATETIME,
					completed_at DATETIME,
					user_id INTEGER`
					);
