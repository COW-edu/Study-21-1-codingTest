#include <stdio.h>
int main()
{
    int n, a[1005], dp[1005], i, j, result[1005];
    scanf("%d",&n);
    
    for(i=1; i<=n; i++) {
        scanf("%d",&a[i]);
    }
    
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for(i=1; i<=n; i++) {
        for(j=4; j<=a[i]; j++) {
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
        }
        result[i] = dp[a[i]];
    }
    
    for(i=1; i<=n; i++) {
        printf("%d\n",result[i]);
    }
    return 0;
}
