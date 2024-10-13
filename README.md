**CarConnect - Car Rental Platform**

Project Overview:

CarConnect is a comprehensive car rental system designed to manage customers, vehicles, reservations, and administrative tasks. This project involves implementing a robust, scalable platform using Python with a strong focus on MSSQL schema design and database interactions.

The application allows users to authenticate, manage vehicles, handle reservations, generate reports, and much more, while adhering to object-oriented programming principles.

**Project Structure**

1. Entity/Model Layer:
   
   Classes that represent the real-world entities of the system.
   
   Classes:
   
           1.Customer: Stores customer details.
           2.Vehicle: Stores vehicle details.
           3.Reservation: Manages reservation details and status.
           4.Admin: Stores administrator details.

2. DAO Layer:
   
   Interfaces and abstract classes that showcase various functionalities with database interaction.
   
   Interfaces & Abstract Classes:
   
           1.ICustomerService
           2.IVehicleService
           3.IReservationService
           4.IAdminService

3. Exception Layer:

   User-defined exceptions to handle various error scenarios.

   Exceptions:

           1.AuthenticationException
           2.ReservationException
           3.VehicleNotFoundException
           4.AdminNotFoundException
           5.InvalidInputException
           6.DatabaseConnectionException

4. Utility Layer:

   Provides reusable utility functions for database connection and property management.

   Classes:

           1.DBPropertyUtil
           2.DBConnUtil

5. Main Layer:

   A MainModule class that demonstrates the functionalities in a menu-driven application.



**Key Functionalities**

1. User Authentication:

           1.Secure login mechanism for customers and admins.
           2.Passwords are stored securely with hashing.

2. Vehicle Management:
   
           1.CRUD operations for vehicles (Create, Read, Update, Delete).
           2.Manage vehicle details including model, make, availability, and pricing.

4. Reservation System:
   
        1.Real-time vehicle reservations with conflict resolution.
        2.Notifications for reservation confirmation via Email/SMS.

6. Reporting:
   
        Generation of reports for reservation history, vehicle utilization, and revenue for admins.


**SQL Schema**

Tables:

1.Customer Table:

        CustomerID, FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate.

2.Vehicle Table:

        VehicleID, Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate.

3.Reservation Table:

        ReservationID, CustomerID (Foreign Key), VehicleID (Foreign Key), StartDate, EndDate, TotalCost, Status.

4.Admin Table:

        AdminID, FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate.


**Unit Testing**

Write NUnit test cases to ensure the correctness and reliability of the system.

**Example Test Cases:**

        1.Test customer authentication with invalid credentials.
        2.Test updating customer information.
        3.Test adding a new vehicle.
        4.Test updating vehicle details.
        5.Test getting a list of available vehicles.
        6.Test generating reports.



**Database Connectivity**

        1.Use the DBConnUtil class to connect to the SQL Server database.
        2.Create and manage connection strings in the DBPropertyUtil class.
        3.Execute SQL queries using the SqlConnection and SqlCommand classes.


**Custom Exceptions**
Use predefined custom exceptions to handle error cases such as:

        1.Incorrect login credentials.
        2.Invalid reservation attempts.
        3.Missing vehicle data.


**How to Run**

        1.Clone the repository or download the project files.
        2.Open the project in your preferred IDE.
        3.Configure the database connection settings in the DBPropertyUtil class.
        4.Run the MainModule class to start the menu-driven application.


**Conclusion**

CarConnect provides a modular and scalable architecture for a car rental platform, supporting secure authentication, vehicle management, real-time reservations, and admin reporting functionalities.
