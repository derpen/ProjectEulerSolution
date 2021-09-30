class Problem3{
	public static void main(String[] args){
		solve(600851475143L);
	}

	public static void solve(long num){
		long result = num;
		for(int i = 1; i < result; i++){
			if(result % 1 == 1){
				break;
			}
			if(result % i == 0){
				result = result / i;
			}
			num = result;
		}
		System.out.println("Result " + result);
	}
}
