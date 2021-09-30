/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

class Problem1{
	public static void main(String[] args){
		solve(1000);
	}

	public static void solve(int limit){
		int ans = 0;
		for(int i = 0; i < limit; i++){
			if(i % 3 == 0){
				ans += i;
			}

			else if(i % 5 == 0){
				ans += i;
			}
		}
		System.out.println("Result " + ans);
	}
}
