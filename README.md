## Flask Application Design: Personal Wallet with Resource Management, Expense Analytics, and Screen Time Monitoring

### Overview:
This Flask application will serve as a personal wallet for users to track their resources, analyze expenses, and monitor screen time. It will provide a user-friendly interface and leverage the Flask framework to handle dynamic data.

### HTML Files:
1. `index.html`: This is the landing page of the application, welcoming users to the personal wallet. It includes navigation links to access different sections of the application.
2. `resources.html`: This page displays the user's resources, such as income, savings, and investments. It allows users to add, edit, and delete resources.
3. `expenses.html`: This page displays the user's expenses, categorized and summarized. Users can add, edit, and delete expenses, as well as generate expense reports.
4. `screen_time.html`: This page displays the user's screen time data, including daily usage, app-wise breakdown, and weekly/monthly summaries.
5. `analytics.html`: This page provides detailed analytics of the user's financial and screen time data. It includes interactive charts, graphs, and insights.

### Routes:
1. `@app.route('/')`: This is the route for the landing page (`index.html`).
2. `@app.route('/resources')`: This route displays the resources page (`resources.html`), allowing users to manage their resources.
3. `@app.route('/expenses')`: This route displays the expenses page (`expenses.html`), enabling users to track and analyze their expenses.
4. `@app.route('/screen_time')`: This route displays the screen time page (`screen_time.html`), providing insights into the user's screen usage.
5. `@app.route('/analytics')`: This route displays the analytics page (`analytics.html`), presenting detailed financial and screen time analytics.
6. `@app.route('/add_resource')`: This route handles adding a new resource to the user's profile.
7. `@app.route('/edit_resource')`: This route handles editing an existing resource.
8. `@app.route('/delete_resource')`: This route handles deleting a resource from the user's profile.
9. `@app.route('/add_expense')`: This route handles adding a new expense to the user's record.
10. `@app.route('/edit_expense')`: This route handles editing an existing expense.
11. `@app.route('/delete_expense')`: This route handles deleting an expense from the user's record.

These HTML files and routes, along with the necessary Flask app logic, will form the foundation of the personal wallet application.