SELECT 
    `players`.`idplayers`,
    `players`.`player_name`,
    `players`.`player_games`,
    `players`.`player_chars`,
    `players`.`username`
FROM
    `upts_s1`.`players`
where username = *;