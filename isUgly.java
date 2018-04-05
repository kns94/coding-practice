class Solution {
    public boolean isPrime(int num){
        for(int i = 2; i < Math.sqrt(num) + 1; i++){
            if(num%i == 0){
                return false;
            }
        }
        return true;
    }

    public boolean isUgly(int num) {
        if(num == 1){
            return true;
        }

        if(num == 0){
            return false;
        }

        while(num % 2 == 0){
            num /= 2;
        }

        while(num % 3 == 0){
            num /= 3;
        }

        while(num % 5 == 0){
            num /= 5;
        }

        if(num == 1){
            return true;
        }
        else{
            return false;
        }
    }
}

class isUglyOutput{
    public static void main(String args[]){
        Solution s = new Solution();
        System.out.println(s.isUgly(6));
    }
}
