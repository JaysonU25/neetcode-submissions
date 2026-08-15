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
    //     for(int i = 0; i < strs.length; i++){
    //         ArrayList ri = new ArrayList<>();
    //         if(strs[i].equals("*")){
    //             System.out.println("Found already");
    //             continue;
    //         } else {
    //             ri.add(strs[i]);
    //             char[] ss = strs[i].toCharArray();
    //             Arrays.sort(ss);
    //             String s = new String(ss);      
    //             h.put(s, strs[i]);
    //         }
    //         for(int j = i+1; j < strs.length; j++){
    //             if(strs[j].equals("*")){
    //                 continue;
    //             } if(strs[i].length() != strs[j].length()){
    //                 continue;
    //             }
    //             char[] ss = strs[j].toCharArray();
    //             Arrays.sort(ss);
    //             String s = new String(ss);
    //             if(h.containsKey(s)){
    //                 ri.add(strs[j]);
    //                 strs[j] = "*";
    //             }
    //         }
    //         strs[i] = "*";
    //         r.add(ri);
    //     }
    //     return r;
    }
}
