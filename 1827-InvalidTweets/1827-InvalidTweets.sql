-- Last updated: 12/29/2025, 1:41:06 AM
# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15