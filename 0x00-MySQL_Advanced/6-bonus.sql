-- script that creates stored procedure AddBonus
-- The script takes 3 inputs
DELIMITER //
CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
)
BEGIN
	IF NOT EXISTS(SELECT name FROM projects WHERE name=project_name) THEN 
		INSERT INTO projects (name) VALUES (project);
	END IF;
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id (SELECT id from projects WHERE name=project_name), score);
END;//
DELIMITER
