class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> r = new ArrayList<>();
        HashMap<String, ArrayList> h = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
                char[] ss = strs[i].toCharArray();
                Arrays.sort(ss);
                String s = new String(ss);   
                if(h.containsKey(s)){
                   ArrayList rip = h.get(s);
                   rip.add(strs[i]);
                   h.put(s,rip);
                }  else{
                    ArrayList ri = new ArrayList<>();
                    ri.add(strs[i]);
                    h.put(s, ri);
                }
        }
        for(String k: h.keySet()){
            r.add(h.get(k));
        }
        return r;
    }
}
