#include <stdio.h>
int main()
{
    int n, a[1005], i, j, dp[1005], max;
    max = 0;
    scanf("%d",&n);
    for(i=1; i<=n; i++) {
        scanf("%d",&a[i]);
    }
    
    for(i=1; i<=n; i++) {
        dp[i] = 1;
        for(j=1; j<=i; j++) {
            if(a[i] > a[j] && dp[i] < dp[j]+1) {
                dp[i]++;
            }
        }
        if(max < dp[i]) {
            max = dp[i];
        }
    }
    printf("%d\n",max);
    return 0;
}
