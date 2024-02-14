-- creates a stored procedure ComputeAverageScoreForUser

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    
    UPDATE users SET average_score = avg_score WHERE id = user_id;
    
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
END$$

DELIMITER ;