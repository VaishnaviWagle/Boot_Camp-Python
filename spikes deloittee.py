num = int(input("enter the length"))
array_nums = list(map(int,input().split()))
spikes = int(input("spikes"))
#new_binary=[]
spike_binary=[]
for i in range (len(array_nums)):
    bin_str = format(array_nums[i],'b')
    #new_binary.append(bin_str)
    #if spikes<=len(bin_str):
    modified_binary=bin_str[:-spikes]
    spike_binary.append(modified_binary)
    final_out = []
    for b in spike_binary:
        if b != '':
            final_out.append(int(b, 2))
        else:
            final_out.append(0)
#print(array_nums)
#print(new_binary)
print(spike_binary)
print(final_out)