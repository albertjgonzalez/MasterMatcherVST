#pragma once

#include <JuceHeader.h>
#include "PluginProcessor.h"

class MatcheringVSTAudioProcessorEditor  : public juce::AudioProcessorEditor
{
public:
    MatcheringVSTAudioProcessorEditor (MatcheringVSTAudioProcessor&);
    ~MatcheringVSTAudioProcessorEditor() override;

    void paint (juce::Graphics&) override;
    void resized() override;

private:
    MatcheringVSTAudioProcessor& audioProcessor;
    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MatcheringVSTAudioProcessorEditor)
};
