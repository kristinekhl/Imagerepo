# Restore
cat backup.sql | docker exec -i imagerepo-db-1 /usr/bin/mysql -u root --password=root images