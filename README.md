# 👔 员工考核管理系统 | Employee Evaluation System

> **基于 Java Web 的员工考核管理系统——绩效考核、评分机制、结果统计、权限管理，助力企业人才管理数字化。**
>
> *Employee evaluation management system based on Java Web — performance review, scoring mechanism, result statistics, permission management, empowering digital talent management.*

---

## ⭐ 核心卖点 | Why Star This

| 卖点 | Feature | 一句话 |
|------|---------|--------|
| 📊 **绩效考核** | Performance Review | 多维度员工绩效考核 |
| ⭐ **评分机制** | Scoring System | 自评 + 上级评分 + 加权汇总 |
| 📈 **结果统计** | Result Stats | 考核结果可视化统计与分析 |
| 🔐 **权限管理** | Permission Control | 管理员/经理/员工分级权限 |
| 🗂️ **完整管理** | Full Management | 部门、员工、考核周期管理 |

---

## 🏆 技术栈 | Tech Stack

![Java](https://img.shields.io/badge/Java-8+-orange?logo=openjdk)
![JSP](https://img.shields.io/badge/JSP-2.3+-blue?logo=java)
![Servlet](https://img.shields.io/badge/Servlet-4.0+-blue?logo=java)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-blue?logo=mysql)
![Maven](https://img.shields.io/badge/Maven-3.6+-red?logo=apachemaven)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.0+-purple?logo=bootstrap)

---

## 🚀 快速开始 | Quick Start

```bash
git clone https://github.com/Windyhhh/Employee-Evaluation-System.git
cd Employee-Evaluation-System

# 1. 初始化数据库
mysql -u root -p < sql/init.sql

# 2. 配置数据库连接
# 编辑 src/main/resources/db.properties

# 3. 编译并部署
mvn clean package
# 将 war 包部署到 Tomcat

# 4. 访问系统
# http://localhost:8080/employee-evaluation
# 默认管理员: admin / admin123
```

---

## 📂 项目结构 | Project Structure

```
Employee-Evaluation-System/
├── src/main/
│   ├── java/com/eval/
│   │   ├── controller/        # 控制器层
│   │   │   ├── LoginController.java
│   │   │   ├── EmployeeController.java
│   │   │   ├── EvaluationController.java
│   │   │   └── StatisticsController.java
│   │   ├── service/           # 业务层
│   │   │   ├── EvaluationService.java
│   │   │   ├── UserService.java
│   │   │   └── StatService.java
│   │   ├── dao/               # 数据访问层
│   │   │   ├── UserDao.java
│   │   │   ├── EvaluationDao.java
│   │   │   └── DeptDao.java
│   │   ├── model/             # 实体类
│   │   │   ├── User.java
│   │   │   ├── Employee.java
│   │   │   └── Evaluation.java
│   │   └── util/              # 工具类
│   ├── resources/
│   │   ├── db.properties
│   │   └── mybatis/
│   └── webapp/
│       ├── WEB-INF/
│       └── views/             # JSP 页面
├── sql/                       # SQL 脚本
└── pom.xml
```

---

## 🔬 核心实现 | Core Implementation

### 考核评分服务 | Evaluation Service

```java
// 绩效考核计算
public class EvaluationService {
    
    public EvaluationResult calculateScore(Evaluation eval) {
        // 多维评分加权
        double selfScore = eval.getSelfScore();     // 自评
        double leaderScore = eval.getLeaderScore(); // 上级评分
        double peerScore = eval.getPeerScore();     // 同级评分
        
        // 权重: 自评20% + 上级60% + 同级20%
        double total = selfScore * 0.2 + leaderScore * 0.6 + peerScore * 0.2;
        
        // 评级
        String grade;
        if (total >= 90) grade = "A (优秀)";
        else if (total >= 80) grade = "B (良好)";
        else if (total >= 70) grade = "C (合格)";
        else grade = "D (需改进)";
        
        return new EvaluationResult(total, grade);
    }
}
```

---

## 🎯 应用场景 | Use Cases

- 🏢 **企业 HR**：员工绩效考核系统
- 🏬 **中小企业**：人事管理数字化
- 🎓 **课程设计**：Java Web 管理系统项目
- 📊 **人才管理**：绩效数据统计与决策

---

## 📄 License

MIT License — 自由使用、修改和分发。

---

> 💡 **Java Web 员工考核系统，Star ⭐ 助力企业人才管理数字化！**
