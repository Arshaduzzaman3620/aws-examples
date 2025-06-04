# 🔐 AWS Classic Networking - Important Port Numbers

A quick reference for commonly used ports in AWS, especially for EC2, RDS, and Security Group setup.

---

## 📦 Common Port Numbers

| Service         | Port | Protocol | Description                           |
|-----------------|------|----------|---------------------------------------|
| SSH             | 22   | TCP      | Secure shell access to Linux EC2      |
| FTP             | 21   | TCP      | File Transfer Protocol (unencrypted)  |
| HTTP            | 80   | TCP      | Web traffic (unencrypted)             |
| HTTPS           | 443  | TCP      | Secure web traffic (SSL/TLS)          |
| RDP             | 3389 | TCP      | Windows Remote Desktop Protocol       |
| MySQL / Aurora  | 3306 | TCP      | MySQL databases                       |
| PostgreSQL      | 5432 | TCP      | PostgreSQL databases                  |
| Oracle DB       | 1521 | TCP      | Oracle RDS                            |
| SQL Server      | 1433 | TCP      | Microsoft SQL Server                  |
| Custom App Port | Any  | TCP/UDP  | Your application (e.g., 5000, 8080)   |

---

## ⚠️ Best Practices

- 🔐 **SSH (22)**, **FTP (21)**, and **RDP (3389)** should be **restricted to your IP**, not open to all.
- 🌍 **HTTP (80)** and **HTTPS (443)** can be public for web apps.
- 🛡️ **Database ports** should be internal only.
- 🔄 **Security Groups are stateful** — return traffic is auto-allowed.
- 🔁 **NACLs are stateless** — define both inbound and outbound rules explicitly.

---

## 📝 For AWS Certification (SAA-C03)

Frequently appears in:
- EC2 setup
- Security Group vs NACL questions
- RDS accessibility settings

---


