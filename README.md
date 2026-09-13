### Запустить всё
docker-compose -f docker-compose.prod.yml up -d

docker-compose -f docker-compose.dev.yml up -d

### Проверить статус
docker-compose ps

### Логи
docker-compose logs -f backend

### Остановить
docker-compose down