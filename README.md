# Shop service
API service for shop management written on DRF

## Getting access

```shell
username: admin
password: 14T5er&P
```

Features
-
-   Модель User(наслідувана від AbstractUser) в окремій прикладній програмі(app user) з переписаним серіалізатором для шифрування паролю. 
-	Token Authentication
-	Реєстрування нового користувача та його вхід(отримання токену після надання credentials)( /api/user/login/)
-	Змінна даних користувача у своєму профілі(/api/user/my-profile/)
-	Permissions (створити новий order може тільки зареєстрований користувач; отримати доступ до свого профілю може тільки зареєстрований користувач)
-	Filters (фільтрування продуктів за категорією; фільтрування списку замовлень за зареєстрованим користувачем)
-	Search (пошук продукта за назвою)
-	При створенні замовлення автоматично присвоюється користувач, який зареєстрований
-	Pagination (для продуктів та замовлень)
-	Routers
-	Upload image (endpoint для завантаження фото продукту)( /api/shop/products/{{ product.id }}/upload-image/)
