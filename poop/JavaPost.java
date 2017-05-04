import java.io.DataOutputStream;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

public class JavaPost {

	public static void main(String[] args) throws IOException {
		// url
		String request = "http://127.0.0.1:3000/msg";
		// parameters
		String urlParameters = "message=" + URLEncoder.encode("poop", "UTF-8");
		
		// set up request
		URL url = new URL(request);
		HttpURLConnection httpCon = (HttpURLConnection) url.openConnection();
		httpCon.setDoOutput(true);
		httpCon.setRequestMethod("POST");
		
		// write parameters
		DataOutputStream wr = new DataOutputStream(
		    httpCon.getOutputStream());
		wr.writeBytes(urlParameters);
		wr.close();

		// make connection, print response
		System.out.println(httpCon.getResponseCode());

		// disconnect
		httpCon.disconnect();
	}

}
