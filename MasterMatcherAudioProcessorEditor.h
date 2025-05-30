#pragma once

#include <JuceHeader.h>
#include "PluginProcessor.h"

class MasterMatcherAudioProcessorEditor  : public juce::AudioProcessorEditor
{
public:
    MasterMatcherAudioProcessorEditor (MasterMatcherAudioProcessor&);
    ~MasterMatcherAudioProcessorEditor() override;

    void paint (juce::Graphics&) override;
    void resized() override;

    void buttonClicked(juce::Button* button) override;

private:
    MasterMatcherAudioProcessor& audioProcessor;
    juce::TextButton loadUserTrackButton { "Load User Track" };
    juce::TextButton loadReferenceTrackButton { "Load Reference Track" };
    juce::TextButton processButton { "Process" };
    juce::Label statusLabel { "Status", "Ready" };

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MasterMatcherAudioProcessorEditor)
};
