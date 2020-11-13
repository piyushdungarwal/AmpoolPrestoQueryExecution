import java.sql.*;
import java.util.Properties;

public class JDBCPresto {

    public static void main(String args[]){
        Connection connection = null;
        Statement statement = null;
        try {
            Class.forName("io.prestosql.jdbc.PrestoDriver");

            Properties properties = new Properties();
            properties.setProperty("user", "admin");
            properties.setProperty("password", "admin");
            properties.setProperty("SSL", "true");
            //properties.setProperty("SSLTrustStorePath", "PATH/ampool_truststore");
            //properties.setProperty("SSLTrustStorePassword", "ampool");
            properties.setProperty("AllowSelfSignedServerCert", "true");
            connection = DriverManager.getConnection("jdbc:presto://<AE master node>:9295/ampool/default", properties);
            statement = connection.createStatement();

            String sql = "show catalogs";
            //String sql = "select * from snowflake.public.warehouse";

            ResultSet resultSet = statement.executeQuery(sql);
            ResultSetMetaData rsmd = resultSet.getMetaData();
            int columnsNumber = rsmd.getColumnCount();
            for (int i = 1; i <= columnsNumber; i++) {
                System.out.print(rsmd.getColumnName(i) + " ");
            }

            System.out.println();
            System.out.println("====================================================");
            while(resultSet.next()){
                for (int i = 1; i <= columnsNumber; i++) {
                    String columnValue = resultSet.getString(i);
                    System.out.print(columnValue + " ");
                }
                System.out.println("");
            }
            resultSet.close();
            statement.close();
            connection.close();
        }catch(SQLException sqlException){
            sqlException.printStackTrace();
        }catch(Exception exception){
            exception.printStackTrace();
        }
    }
}
