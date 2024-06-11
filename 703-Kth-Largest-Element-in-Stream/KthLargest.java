class KthLargest {
    // Create the heap and k element
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        for (int i: nums){
            minHeap.add(i);
            // Limit size of minHeap to K
            if (minHeap.size() > k)
                minHeap.poll();
        }
    }
    
    public int add(int val) {
        // Call to method will add val to heap
        minHeap.add(val);

        // Remove k + 1 largest val from heap
        if (minHeap.size() > k)
            minHeap.poll();

        // Return Kth largest
        return minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
