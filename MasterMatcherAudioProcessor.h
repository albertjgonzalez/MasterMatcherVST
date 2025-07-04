#pragma once

#include <JuceHeader.h>
#include <string>
#include <memory>

class MasterMatcherAudioProcessor : public juce::AudioProcessor
{
public:
    MasterMatcherAudioProcessor();
    ~MasterMatcherAudioProcessor() override;

    void prepareToPlay (double sampleRate, int samplesPerBlock) override;
    void releaseResources() override;

    bool isBusesLayoutSupported (const BusesLayout& layouts) const override;
    void processBlock (juce::AudioBuffer<float>&, juce::MidiBuffer&) override;

    juce::AudioProcessorEditor* createEditor() override;
    bool hasEditor() const override;

    const juce::String getName() const override;
    bool acceptsMidi() const override;
    bool producesMidi() const override;
    double getTailLengthSeconds() const override;

    int getNumPrograms() override;
    int getCurrentProgram() override;
    void setCurrentProgram (int index) override;
    const juce::String getProgramName (int index) override;
    void changeProgramName (int index, const juce::String& newName) override;

    void getStateInformation (juce::MemoryBlock& destData) override;
    void setStateInformation (const void* data, int sizeInBytes) override;

    // Audio file management
    bool loadUserTrack(const juce::File& file);
    bool loadReferenceTrack(const juce::File& file);
    bool processTracks();
    juce::File getProcessedTrack() const;

private:
    juce::File userTrackFile;
    juce::File referenceTrackFile;
    juce::File processedTrackFile;
    bool isProcessing = false;
    std::unique_ptr<juce::Thread> processingThread;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MasterMatcherAudioProcessor)
};
