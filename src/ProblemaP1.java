
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class ProblemaP1 {

    static final long INF = Long.MAX_VALUE / 2;

    public static void main(String[] args) throws Exception {
        ProblemaP1 instancia = new ProblemaP1();
        try (InputStreamReader is = new InputStreamReader(System.in); BufferedReader br = new BufferedReader(is);) {
            String line = br.readLine();
            int casos = Integer.parseInt(line);
            line = br.readLine();
            for (int i = 0; i < casos && line != null && line.length() > 0 && !"0".equals(line); i++) {
                final String[] dataStr = line.split(" ");
                final int[] numeros = Arrays.stream(dataStr).mapToInt(f -> Integer.parseInt(f)).toArray();
                int n = numeros[0];

                int j = numeros[1];

                int m = numeros[2];

                int[] arr = new int[n];

                for (int k = 0; k < n; k++) {
                    arr[k] = numeros[k + 3];
                }
                long respuesta = instancia.minimo(n, j, m, arr);
                System.out.println(respuesta);
                line = br.readLine();
            }
        }

    }

    public long minimo(int n, int j, int m, int[] numeros) {
        long[][][] dp = new long[n + 1][j + 1][m + 1];

        for (int i = 0; i <= n; i++) {
            for (int k = 0; k <= j; k++) {
                Arrays.fill(dp[i][k], INF);
            }
        }
        dp[0][0][0] = 0;

        for (int i = 0; i < n; i++) {
            for (int k = 0; k <= j; k++) {
                for (int c = 0; c <= m; c++) {

                    if (dp[i][k][c] == INF) {
                        continue;
                    }
                    if (dp[i][k][c] < dp[i + 1][k][c]) {
                        dp[i + 1][k][c] = dp[i][k][c];

                    }

                    if (k < j) {
                        int costoAdicional = i - k;
                        if (c + costoAdicional <= m) {
                            int nuevoCosto = c + costoAdicional;
                            long nuevaSuma = dp[i][k][c] + numeros[i];
                            if (nuevaSuma < dp[i + 1][k + 1][nuevoCosto]) {
                                dp[i + 1][k + 1][nuevoCosto] = nuevaSuma;

                            }
                        }
                    }

                }
            }
        }

        long respuesta = INF;
        for (int c = 0; c <= m; c++) {
            respuesta = Math.min(respuesta, dp[n][j][c]);
        }

        return respuesta;
    }
}
