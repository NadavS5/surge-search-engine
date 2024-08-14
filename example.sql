INSERT INTO websites (url,title,keywords) VALUES ("google.com","google","search engine google ")

INSERT INTO keywords (keyword) VALUES ("google") --Keywords--
INSERT INTO keywords (keyword) VALUES ("search")
INSERT INTO keywords (keyword) VALUES ("engine")

INSERT INTO keyword_website_map (keyword_id,website_id,tf) VALUES (1,1,1) --Keyword Id Website Id Relevance score--



SELECT d.url, d.title, kdm.relevance_score
FROM keyword_document_map kdm
JOIN keywords k ON kdm.keyword_id = k.id
JOIN documents d ON kdm.document_id = d.id
WHERE k.keyword = 'example'
ORDER BY kdm.relevance_score DESC;
