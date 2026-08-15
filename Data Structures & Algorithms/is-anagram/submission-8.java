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
    }
}
