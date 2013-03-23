import model


db = model.connect_db()

user_id = model.new_user(db, 
						"chriszf@gmail.com", 
						"securepassword", 
						"Christian")

task = model.new_task(db, 
					  "Complete this task list", 
					  user_id)

user_id2 = model.new_user(db,
						  "mdeegill@gmail.com",
						  "password2",
						  "Dee")

task2 = model.new_task(db,
					   "Complete this now",
					   user_id2)

task3 = model.new_task(db,
					   "You have no tasks bc you crushed them all already.",
					   1)