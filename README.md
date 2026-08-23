# 👔 Employee Evaluation System | 员工评价管理系统

> **Comprehensive employee performance evaluation management system. Java Web application with employee management, performance scoring, evaluation criteria, reporting, and statistics. MySQL database, MVC architecture.**
>
> 综合员工绩效评价管理系统。Java Web 应用，包含员工管理、绩效评分、评价标准、报表和统计。MySQL 数据库，MVC 架构。

---

## 🌟 Features | 核心特性

- **Employee Management** — CRUD for employee records
- **Performance Evaluation** — Multi-criteria scoring system
- **Evaluation Criteria** — Customizable KPIs and weights
- **Reporting** — Performance reports and rankings
- **Statistics** — Department/team performance analytics
- **Role-Based Access** — Admin, manager, employee roles
- **Java Web** — Servlet + JSP + MySQL

---

## 🚀 Quick Start | 快速开始

```bash
# Import database
mysql -u root -p < database/employee_eval.sql

# Build and deploy to Tomcat
mvn clean package
cp target/employee-eval.war $TOMCAT_HOME/webapps/

# Access
# http://localhost:8080/employee-eval/
```

---

## 📄 License | 许可证

MIT License.

[GitHub](https://github.com/Windyhhh/Employee-Evaluation-System)
