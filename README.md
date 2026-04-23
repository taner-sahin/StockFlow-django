📦 StockFlow

A backend-focused Django e-commerce project designed to simulate a real-world shopping flow, including stock management, a database-driven cart system, and order processing.

🧠 About

StockFlow focuses on one of the most critical parts of an e-commerce system: stock management.

It implements a complete backend flow:

Product → Cart → Order → Stock update
Prevents adding more items than available stock
Automatically reduces stock after checkout
Ensures user-based data isolation
⚙️ Core Features
🔐 Authentication
User registration / login / logout
Protected cart and order operations
🧭 Dynamic Structure
Dynamic navbar (categories, cart count, order count)
Dynamic homepage
Category-based product filtering
Product detail pages (slug-based)
🛒 Cart System (Database-Based)
Fully database-driven cart system
Add / increase / decrease / remove items
Same product does not create a new row → quantity increases
User-specific cart logic
Dynamic cart count in navbar
📦 Order System
Order model
OrderItem model
Snapshot logic (stores product name & price at purchase time)
Checkout system (cart → order conversion)
Automatic cart cleanup after checkout
📊 Order Management
"My Orders" page
Order detail page
Order status system:
pending
preparing
shipped
delivered
Dynamic order count in navbar
Order statistics dashboard
🔥 Backend Highlights
Stock control enforced at cart level
Users cannot add more items than available stock
Stock is automatically reduced after checkout
Only authenticated users can access cart and orders
Users can only view their own orders
🔄 Order Flow
User logs in
Adds products to cart
Cart items are stored in database
User proceeds to checkout
Order is created
OrderItems are generated (with snapshot data)
Total price is calculated
Stock is reduced
Cart is cleared
🧱 Tech Stack
Python
Django
Bootstrap
SQLite
📁 Project Structure
products → product listing, filtering, detail pages
cart → database-based cart system
orders → order creation, checkout, order history
🎯 What I Learned
Building a database-driven cart system
Designing an order architecture
Implementing stock management logic
Using snapshot data in e-commerce systems
Connecting cart flow to checkout process
Managing user-based data securely
Using context processors for global data
📌 Status

✅ Backend core completed
✅ Full e-commerce flow implemented

StockFlow is completed as a backend-focused project that simulates a real-world e-commerce system.

🗺️ Roadmap
Project 1 → StepCart
Project 2 → OrderCore
Project 3 → StockFlow ✅
Project 4 → CouponCart (Coupon System) ⏳
👨‍💻 Author

Taner Sahin
GitHub: https://github.com/TanerSahin19

🚀 Final Note

This project demonstrates real backend development skills:

Cart system logic
Order processing
Stock control
Clean backend architecture