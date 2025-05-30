#include "PluginProcessor.h"
#include "PluginEditor.h"

MatcheringVSTAudioProcessor::MatcheringVSTAudioProcessor()
    : AudioProcessor (BusesProperties()
                     #if ! JucePlugin_IsMidiEffect
                      #if ! JucePlugin_IsSynth
                       .withInput  ("Input",  AudioChannelSet::stereo(), true)
                      #endif
                       .withOutput ("Output", AudioChannelSet::stereo(), true)
                     #endif
                       )
{
}

MatcheringVSTAudioProcessor::~MatcheringVSTAudioProcessor()
{
}

void MatcheringVSTAudioProcessor::prepareToPlay (double sampleRate, int samplesPerBlock)
{
}

void MatcheringVSTAudioProcessor::releaseResources()
{
}

bool MatcheringVSTAudioProcessor::isBusesLayoutSupported (const BusesLayout& layouts) const
{
    if (layouts.getMainOutputChannelSet() != AudioChannelSet::stereo())
        return false;

    if (layouts.getMainInputChannelSet() != AudioChannelSet::stereo())
        return false;

    return true;
}

void MatcheringVSTAudioProcessor::processBlock (AudioBuffer<float>& buffer, MidiBuffer& midiMessages)
{
    juce::ScopedNoDenormals noDenormals;
    auto totalNumInputChannels  = getTotalNumInputChannels();
    auto totalNumOutputChannels = getTotalNumOutputChannels();

    for (auto i = totalNumInputChannels; i < totalNumOutputChannels; ++i)
        buffer.clear (i, 0, buffer.getNumSamples());
}

juce::AudioProcessorEditor* MatcheringVSTAudioProcessor::createEditor()
{
    return new MatcheringVSTAudioProcessorEditor (*this);
}

bool MatcheringVSTAudioProcessor::hasEditor() const
{
    return true;
}

const juce::String MatcheringVSTAudioProcessor::getName() const
{
    return JucePlugin_Name;
}

bool MatcheringVSTAudioProcessor::acceptsMidi() const
{
    return false;
}

bool MatcheringVSTAudioProcessor::producesMidi() const
{
    return false;
}

double MatcheringVSTAudioProcessor::getTailLengthSeconds() const
{
    return 0.0;
}

int MatcheringVSTAudioProcessor::getNumPrograms()
{
    return 1;
}

int MatcheringVSTAudioProcessor::getCurrentProgram()
{
    return 0;
}

void MatcheringVSTAudioProcessor::setCurrentProgram (int index)
{
}

const juce::String MatcheringVSTAudioProcessor::getProgramName (int index)
{
    return "Program " + (index + 1);
}

void MatcheringVSTAudioProcessor::changeProgramName (int index, const juce::String& newName)
{
}

void MatcheringVSTAudioProcessor::getStateInformation (juce::MemoryBlock& destData)
{
}

void MatcheringVSTAudioProcessor::setStateInformation (const void* data, int sizeInBytes)
{
}
