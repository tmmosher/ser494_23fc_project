import wf_datagen, wf_dataprocessing, wf_visualization

if __name__ == '__main__':
    wf_datagen.generate()
    wf_dataprocessing.munge()
    wf_visualization.visualize()