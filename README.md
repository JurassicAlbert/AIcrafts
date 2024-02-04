# AIcrafts

## What I'm Creating?

AIcrafts is an innovative e-commerce platform that focuses on selling customizable T-shirts. Users can choose from a curated selection of pre-designed shirts available in the store. Additionally, they have the option to unleash their creativity using an intuitive editor on the website to design their own personalized T-shirts. What sets AIcrafts apart is the integration of artificial intelligence, allowing users to generate unique designs through language models.

## Why I'm Creating This?

The aim of AIcrafts is to provide a dynamic and engaging shopping experience for users who seek both curated and personalized T-shirt designs. By combining the power of Django and Vue.js, the platform aims to offer a seamless and user-friendly interface for designing and purchasing custom T-shirts.

## How I'm Creating This?

### Backend (Django/DRF):

- **Django**: A high-level Python web framework for building robust and scalable web applications.
- **Django Rest Framework (DRF)**: A powerful and flexible toolkit for building Web APIs in Django.

### Frontend (Vue.js):

- **Vue.js**: A progressive JavaScript framework for building user interfaces, providing a reactive and efficient way to create interactive web applications.

### Database:

- **SQLite (Development)**: Lightweight and easy to set up for development purposes.
- **PostgreSQL (Production)**: A robust, open-source relational database system for scalability and performance.

### Authentication:

- **Django Allauth**: An integrated set of Django applications addressing authentication, registration, account management, and more.

### AI Integration:

- **IN PROGRESS**: Integration with OpenAI GPT-3.5 for generating T-shirt designs.

## TODO

### Backend:

- [ ] Implement Django models for T-shirts, user profiles, and orders.
- [ ] Develop API endpoints for CRUD operations on T-shirts and user interactions.
- [ ] Integrate Django Allauth for user authentication and registration.
- [ ] Set up the database and migrations.

### Frontend:

- [ ] Create Vue.js components for the T-shirt editor, product listing, and user authentication.
- [ ] Implement API calls to retrieve and display T-shirt data.
- [ ] Design responsive and user-friendly UI/UX.
- [ ] Integrate the OpenAI GPT-3.5 model for generating T-shirt designs.

### General:

- [ ] Set up project directory structure.
- [ ] Configure development and production settings.
- [ ] Implement proper error handling and validation.
- [ ] Write comprehensive tests for backend and frontend functionality.
- [ ] Deploy the application to a production server.

## Endpoints

### Users:
1. **GET /api/users/:id** - Get information about a user with a specific ID.
2. **POST /api/users/register** - Register a new user.
3. **POST /api/users/login** - Log in a user and obtain an access token.
4. **GET /api/users/profile** - Get information about the currently logged-in user.
5. **PUT /api/users/:id** - Update user information for a specific ID.

### Products:
6. **GET /api/products** - Get a list of all products (T-shirts) in the store.
7. **GET /api/products/:id** - Get information about a specific product (T-shirt).
8. **POST /api/products** - Add a new product (T-shirt).
9. **PUT /api/products/:id** - Update information about a product (T-shirt) with a specific ID.
10. **DELETE /api/products/:id** - Delete a product (T-shirt) with a specific ID.

### Orders:
11. **GET /api/orders** - Get a list of all user orders.
12. **GET /api/orders/:id** - Get details of an order with a specific ID.
13. **POST /api/orders** - Place a new order.

### Store T-shirts:
14. **GET /api/store-shirts** - Get a list of available T-shirts in the store.
15. **GET /api/store-shirts/:id** - Get details of a specific T-shirt available in the store.

### T-shirt Editor:
16. **POST /api/editor/generate-design** - Generate a T-shirt design using artificial intelligence.
17. **POST /api/editor/save-design** - Save a T-shirt design created in the editor.
