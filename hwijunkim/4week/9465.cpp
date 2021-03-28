#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
    int t, n, a[5][100005], dp[5][100005], i, j;
    scanf("%d",&t);
    for(i=1; i<=t; i++) {
        scanf("%d",&n);
        for(j=1; j<=n; j++) {
            scanf("%d",&a[1][j]);
        }
        for(j=1; j<=n; j++) {
            scanf("%d",&a[2][j]);
        }
        
        dp[1][1] = a[1][1];
        dp[2][1] = a[2][1];
        dp[1][2] = a[2][1] + a[1][2];
        dp[2][2] = a[1][1] + a[2][2];
        
        for(j=3; j<=n; j++) {
            dp[1][j] = a[1][j] + max(dp[2][j-1], dp[2][j-2]);
            dp[2][j] = a[2][j] + max(dp[1][j-1], dp[1][j-2]);
        }
        
        printf("%d\n",max(dp[1][n],dp[2][n]));
    }
    return 0;
}
