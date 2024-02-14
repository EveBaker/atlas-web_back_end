-- SQL that creates a stored procedure AddBonus 

DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- checks if project exists, then it looks for its ID
    SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;

    -- if the project is not a thing, it insterts then gets the ID
    IF project_id IS NULL then
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- inserts correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
    END $$

DELIMITER ;