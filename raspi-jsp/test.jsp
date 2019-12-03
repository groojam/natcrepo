<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>어항관리</title>
</head>
<body>
    <%
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        int count = 1;
        
        try{
            String jdbcDriver = "jdbc:mysql://18.216.172.165:3306/raspi_db?serverTimezone=Asia/Seoul";
            String dbUser = "pi";
            String dbPwd = "pikey999";
             
            conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPwd);
             
            pstmt = conn.prepareStatement("select * from tmp order by time desc");
             
            rs = pstmt.executeQuery();
             
            while(rs.next() && count <= 1){
    %>

     <%= rs.getString("temp_c") + "℃" + " / "%>
     <%= rs.getString("temp_f") + "℉"%>

    <%
            }
        }catch(SQLException se){
            se.printStackTrace();
        }finally{
            if(rs != null) rs.close();
            if(pstmt != null) pstmt.close();
            if(conn != null) conn.close();
        }
    %>
</body>
</html>