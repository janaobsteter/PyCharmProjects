import imcmc

image = imcmc.load_image('/home/jana/Downloads/Alpha-logo-blue-01.png', 'L')

# This call is random -- rerun adjusting parameters until the image looks good
trace = imcmc.sample_grayscale(image, samples=100000, tune=500, nchains=2)

# Lots of plotting options!
fig, ax = imcmc.plot_multitrace(trace, image, marker='o', markersize=5,
                      colors=['#353097'], alpha=0.4);
fig, ax = imcmc.plot_multitrace(trace, image, marker='o', markersize=10,
                      colors=['#353097'], alpha=0.4, linestyle='-');
fig.show()

# Save as a gif, with the same arguments as above, plus some more
imcmc.make_gif(trace, image, dpi=40, marker='o', markersize=5,linestyle='-',
               colors=['#353097'], alpha=0.4,
               filename='AlphaGenes_lines.gif')