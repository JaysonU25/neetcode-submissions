class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }


        char[] ss = s.toCharArray();
        Arrays.sort(ss);
        char[] tt = t.toCharArray();
        Arrays.sort(tt);

        String new_s = new String(ss);
        String new_t = new String(tt);

        if(new_s.equals(new_t)){
            return true;
            } else{
                return false;
            }
        
        // for(int i = 0; i < s.length(); i++){
        //     for(int j = 0; j < t.length(); j++){
        //         if(s.charAt(i) == t.charAt(j)){
        //             s = replaceCharacter(s,i);
        //             t = replaceCharacter(t,j);
        //             break;
        //         }
        //         if(j == t.length()-1){
        //             return false;
        //         }
        //     }
        // }
        // if(s.charAt(s.length()-1) != '*'){
        //     return false;
        // } else{
        //     return true;
        // }
    }

    // public static String replaceCharacter(String s, int i){
    //     if(i == 0){
    //         return "*" + s.substring(1);
    //     }
    //     return s.substring(0,i) + "*" + s.substring(i+1);
    // }
}
