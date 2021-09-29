class Problem2{
	public static void main(String[] args){
		solve(4000000);
	}

	public static void solve(int limit){
		int i = 1;
		int j = 2;
		int ans = 0;
		while(true){
			if(j>limit){
				break;
			}
			if(j%2==0){
				ans += j;
			}
			i = j;
			j = i + j;
		}
		System.out.println(ans);
	}
}
