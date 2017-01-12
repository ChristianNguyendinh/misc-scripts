import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/*
Mostly a copy pasta from the Java SQLite JDBC Driver by Taro L. Saito, 
for future reference
Requires the SQLite JDBC library to be downloaded, then the jar file
to be added to the project's classpath.
*/

public class ServerConnection {

    public static void main(String[] args) throws ClassNotFoundException{
        Class.forName("org.sqlite.JDBC");

        Connection connection = null;
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:<PATH TO DB>");
            Statement statement = connection.createStatement();
            statement.setQueryTimeout(10);
            //statement.executeUpdate("INSERT INTO testing (name) VALUES (\"Bawb\")");

            ResultSet rs = statement.executeQuery("SELECT * FROM testing");
            while(rs.next()) {
                System.out.print("id : " + rs.getString("id") + " | ");
                System.out.println("name : " + rs.getString("name"));
            }

        } catch (SQLException e) {
            System.err.println(e.getMessage());

        } finally {
            try {
                if (connection != null)
                    connection.close();

            } catch (SQLException e) {
                System.err.println(e);

            }
        }
    }

}