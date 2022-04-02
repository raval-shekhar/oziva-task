# To scale to million user i will consider following points
 - Putting proper indexes on database
 - Replication of database for disaster recovery
 - Create Read replicas for faster reads
 - Sharding of database (To minimize reads of whole table)
 - Putting cache of non frequently used data (With help of redis)
 - Serving posts made by users through CDN (Like AWS cloudfront)
 - Scale architecture with microservices (Like each part can scale independently -> posts, comments and follow/follower)