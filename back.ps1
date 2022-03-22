# Backup

if( $args[0] -eq "backup" ){
    docker exec imagerepo-db-1 /usr/bin/mysqldump -u root --password=root images > backup.sql
}

# Restore
elseif( $args[0] -eq "restore" ){
cat backup.sql | docker exec -i imagerepo-db-1 /usr/bin/mysql -u root --password=root images
}